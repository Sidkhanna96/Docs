import fs from "fs";
import readline from "readline";

class LogRepo {
  constructor() {
    this._file = "./src/Database/log.txt";
  }

  async parseTxt() {
    const structuredLogs = [];
    const fileStream = fs.createReadStream(this._file, { encoding: "utf8" });

    const rl = readline.createInterface({
      input: fileStream,
      crlfDelay: Infinity,
    });

    for await (const line of rl) {
      if (!line.trim()) continue;

      const [date, time, level, ...rest] = line.split(/\s+/);
      const timestamp = `${date} ${time}`;

      const record = {}; // define record for this line
      rest.forEach((pair) => {
        const [key, value] = pair.split("=");
        if (value !== undefined)
          record[key] = isNaN(value) ? value : Number(value);
      });

      structuredLogs.push({ timestamp, level, ...record });
    }

    return structuredLogs;
  }
}

export default LogRepo;
