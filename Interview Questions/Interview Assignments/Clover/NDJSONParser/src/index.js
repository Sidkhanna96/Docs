// First extract the format of the spec files
// Search files if exist
// Pull data from the data files
// Create NDJSON data in output folder

const { SpecParser } = require("./Components/SpecParser");
const { InputInterpreter } = require("./Components/InputInterpreter");

main = async () => {
  const spec = new SpecParser();

  // Fetch all the spec files
  const files = await spec.fetchFiles();
  // Get all the data
  const fileSchema = await Promise.all(
    files.map(async (file) => {
      const columns = await spec.fetchDataStructure(file);

      // Removes the elements from the last index of extension
      const fileWithoutExtension = file.split(".").slice(0, -1).join(".");

      return { [fileWithoutExtension]: columns };
    })
  );

  // Prints out each column schema def
  console.log(JSON.stringify(fileSchema));

  // Testing if we get an empty file with no data in the data folder
  // Does not validate if the file sent
  fileSchema.push({ fake: [{}] });

  const inputFiles = new InputInterpreter();

  fileSchema.forEach(async (file) => {
    const keyFileSchema = Object.keys(file)[0];

    // Check if the schema definition are true if the files exist in the dataSource
    // filters out the files that do exist in the data source
    const associatedInputFiles = await inputFiles.fileExist(
      keyFileSchema,
      "./data/"
    );

    if (associatedInputFiles.length > 0) {
      // For each file do an output to the output folder
      associatedInputFiles.forEach(async (iFile) => {
        await inputFiles.formatInputFile(iFile, file[keyFileSchema]);
      });
    }
  });
};

main();
