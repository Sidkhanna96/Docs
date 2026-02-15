import fs from "fs";
import { parse } from "csv-parse";

class csvRepo {
  constructor() {
    this._fileDir = "./src/Database/file.csv";
  }

  parseCsv() {
    return new Promise((resolve, reject) => {
      const data = [];

      fs.createReadStream(this._fileDir)
        .pipe(parse({ delimiter: [",", ";"], columns: true }))
        .on("data", (row) => {
          data.push(row);
        })
        .on("end", () => {
          resolve(data);
        })
        .on("error", (err) => {
          reject(err);
        });
    });
  }
}

export default csvRepo;
