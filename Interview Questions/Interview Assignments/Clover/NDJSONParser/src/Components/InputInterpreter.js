const { glob } = require("glob");
const fs = require("fs");
const readline = require("readline");
const { v4: uuidv4 } = require("uuid");
const path = require("path");

const convertDataType = (cellType, cell) => {
  switch (cellType.toUpperCase()) {
    case "TEXT":
    case "STRING":
      return String(cell).trim();
    case "BOOLEAN":
      return cell === "true" || cell === "1";
    case "INTEGER":
      return parseInt(cell);
    default:
      throw new Error("Unsupported data type");
  }
};

/**
 * create input file data
 */
class InputInterpreter {
  /**
   *
   * @param {*} fileName
   * @param {*} filePath
   * @returns
   */
  async fileExist(fileName, filePath) {
    const pathCheck = filePath + fileName + "*";
    return await glob(pathCheck, (err, files) => {
      if (err) {
        reject(err);
        return;
      }
      return files;
    });
  }

  /**
   *
   * @param {*} iFileName
   * @param {*} fileSchema
   */
  async formatInputFile(iFileName, fileSchema) {
    const tempFileName = path.join("./output/", uuidv4() + ".tmp");

    // Reading from input file
    const fileStream = fs.createReadStream(iFileName);
    const r1 = readline.createInterface({
      input: fileStream,
      crlfDelay: Infinity, // \r\n both recognized as newline
    });

    for await (let line of r1) {
      const NDJSON = {};

      for (const cType in fileSchema) {
        const columnType = fileSchema[cType];
        const column_name = columnType["column name"];
        const width = columnType["width"];
        const datatype = columnType["datatype"];

        const cell = line.substring(0, convertDataType("INTEGER", width));
        line = line.substring(convertDataType("INTEGER", width));

        NDJSON[column_name] = convertDataType(datatype, cell);
      }

      // Write to the temporary file
      fs.appendFileSync(tempFileName, JSON.stringify(NDJSON) + "\n");
    }

    const newIFileName =
      "./output/" +
      iFileName.replace("data/", "").replace(".txt", "") +
      ".ndjson";

    // Rename the temporary file to the actual file path
    fs.renameSync(tempFileName, newIFileName);
  }
}

module.exports = { InputInterpreter };
