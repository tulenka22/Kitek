const toParse = `<TABLE>`;

const fs = require("fs");

let parsed = [];

for (let row of toParse.split("\n")) {
  const th = row.split("\t");
  const generated_td = th.map(
    (t) =>
      ` <td class="a-table__cell a-table__cell-8 a-table__cell-center">${t}</td>`
  );
  parsed.push(`<tr>${generated_td.join("\n")}</tr>`);
}
fs.writeFileSync("parsed.html", parsed.join("\n"));
