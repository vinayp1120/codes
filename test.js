const d = new Date();
console.log(d);
console.log(d.getTime());
console.log(d.getTimezoneOffset());
console.log(d.getTimezoneOffset() / 60); // why divide by 60? because getTimezoneOffset returns the offset in minutes, so dividing by 60 converts it to hours.
console.log(d.getTimezoneOffset() / 60 * -1); // why multiply by -1? because getTimezoneOffset returns the offset in minutes, and it is positive if the local timezone is behind UTC and negative if it is ahead of UTC. Multiplying by -1 converts it to a positive value for timezones ahead of UTC and a negative value for timezones behind UTC.
console.log(d.getDay()); // returns the day of the week (0-6) where 0 is Sunday and 6 is Saturday
console.log(d.getDate()); // returns the day of the month (1-31)
console.log(d.getMonth()); // returns the month (0-11) where 0 is January and 11 is December
console.log(d.getFullYear());
console.log("Hello, World!");console.log("Hello, World!");console.log("Hello, World!");console.log("Hello, World!");console.log("Hello, World!");console.log("Hello, World!");console.log("Hello, World!");console.log("Hello, World!");console.log("Hello, World!");console.log("Hello, World!");console.log("Hello, World!");console.log("Hello, World!");