async function csvHandler(req, res, next) {
  const { csvRepo } = req.context;
  const data = await csvRepo.parseCsv();

  const summation = {};

  data.forEach((person) => {
    if (summation[person.department] === undefined) {
      summation[person.department] = [];
    }
    summation[person.department].push(person.salary);
  });

  Object.keys(summation).forEach((key) => {
    const res = summation[key].reduce((acc, cur) => acc + parseInt(cur), 0);
    summation[key] = res / summation[key].length;
  });

  res.send(summation);

  next();
}

export default csvHandler;
