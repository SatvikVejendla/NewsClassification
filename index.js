const executePython = require("./train/exec.js");
const load = require("./model/load.js");

let arg = process.argv.slice(2) || 0;

let promise = function () {
  return new Promise((resolve) => resolve());
};

if (/--?r(|e|etrain)/g.test(arg)) {
  console.log("Retraining model...");
  promise = executePython;
}
promise().then(() => load().then(() => require("./server/app.js")));
