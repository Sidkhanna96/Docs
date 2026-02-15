async function logHandler(req, res, next) {
  const { logRepo } = req.context;
  const data = await logRepo.parseTxt();

  const userError = {};

  data.forEach((d) => {
    if (d.level === "ERROR") {
      if (userError[d.user_id] === undefined) {
        userError[d.user_id] = 0;
      }
      userError[d.user_id] += 1;
    }
  });

  res.send(userError);

  next();
}

export default logHandler;
