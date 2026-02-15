const fs = require("fs");
const util = require("util");
const { parse } = require("csv-parse");
const { finished } = require("stream/promises");

// Promisify - so can use async await/promise - instead of utilizing the inbuilt callback function
const readdir = util.promisify(fs.readdir);
// const createReadStream = util.promisify(fs.createReadStream)

/**
 * Used to Fetch the specs of all the files provided in the specs file
 *
 */
class SpecParser {
  /**
   * Fetch files
   * @returns
   */
  async fetchFiles() {
    // Fetch all files in specs folder
    const dirents = await readdir("./specs", { withFileTypes: true });
    const files = dirents
      .filter(
        // only select files and filter out hidden files through regex
        (dirent) => dirent.isFile() && !/(^|\/)\.[^\/\.]/g.test(dirent.name)
      )
      .map((dirent) => dirent.name);

    return files;
  }

  /**
   * Check what actual columns are there
   * @param {*} file
   * @returns
   */
  async fetchDataStructure(file) {
    // Find each column specification - the order of the data returned matters
    this.data = [];
    // we open the file
    const parsingFile = fs
      .createReadStream("./specs/" + file)
      // assumes that the records are separated by following data
      // pipe enables to stream data in process
      .pipe(
        parse({
          deliminator: [";", ",", ":", "|", "\t"],
          // This enables to parse the data in csv in column manner
          columns: true,
        })
      )
      // Get all the data
      .on("data", (data) => {
        this.data.push(data);
      });

    await finished(parsingFile);
    return this.data;
  }
}

module.exports = { SpecParser };
