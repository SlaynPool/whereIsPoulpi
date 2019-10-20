const Discord = require("discord.js");
const client = new Discord.Client();
 
client.on("ready", () => {
    console.log("I am ready! ");
});
 
client.on("message", (message) => {
  if (message.content.startsWith("whereIsPoulpi")) {
    message.channel.send("poulpi location be find here : un-site.com");
  }
});
 
client.login("SuperSecretBotTokenHere");
