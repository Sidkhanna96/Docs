import express from "express";
import csvHandler from "./handler/csvHandler.js";
import logHandler from "./handler/logHandler.js";

const route = express.Router();

route.get("/csv", csvHandler);
route.get("/log", logHandler);

export default route;
