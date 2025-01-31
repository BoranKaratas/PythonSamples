/* global use, db */
// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use('bokaDB');

// Insert a few documents into the sales collection.
db.getCollection('users').insertMany([
  { 'boran': 'boran@example.com', 'insertdate': new Date('2025-01-31T11:52:00Z') },
]);

// Run a find command to view items sold on April 4th, 2014.
const userList = db.getCollection('users').find({
  date: { $gte: new Date('2025-01-01'), $lt: new Date('2026-01-01') }
}).count();

// Print a message to the output window.
console.log(`${userList} Kullanıcı listesi bu şekildedir.`);

// Here we run an aggregation and open a cursor to the results.
// Use '.toArray()' to exhaust the cursor to return the whole result set.
// You can use '.hasNext()/.next()' to iterate through the cursor page by page.