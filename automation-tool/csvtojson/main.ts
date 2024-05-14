import fs from "fs-extra";

const flattenObj = (ob: any) => {
  let result = {};

  // loop through the object "ob"
  for (const i in ob) {
    // We check the type of the i using
    // typeof() function and recursively
    // call the function again
    if (typeof ob[i] === "object" && !Array.isArray(ob[i])) {
      const temp = flattenObj(ob[i]);
      for (const j in temp) {
        // Store temp in result
        result[i + "." + j] = temp[j];
      }
    }

    // Else store ob[i] in result directly
    else {
      result[i] = ob[i];
    }
  }
  return result;
};

async function main(fileinput: string, fileoutput: string) {
  const ob = await fs.readJson(fileinput);
  const result = ob.map((a) => flattenObj(a));
  await fs.createFile(fileoutput);
  await fs.writeFile(fileoutput, JSON.stringify(result));
}

main("./dump/YPL/YPL.chats.json", "chats.json");
