import express from "express";
import routes from "./Routes/routes.js";
import csvRepo from "./Repos/csvRepo.js";
import logRepo from "./Repos/logRepo.js";
import cors from "cors";

const app = express();

app.use(cors());

app.use((req, res, next) => {
  req.context = {
    csvRepo: new csvRepo(),
    logRepo: new logRepo(),
  };
  next();
});

app.use("/v1", routes);

const server = app.listen(3000, () => {
  console.log("listening on port:3000");
});

server.on("error", (err) => {
  console.error("Server error", err);
  process.exit(1);
});
