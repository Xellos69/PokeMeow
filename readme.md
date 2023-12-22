# PokeGrinder V2
An Auto-Grinding Self-Bot for the Discord Bot PokéMeow. As efficient as can be.
Now in Golang for better handling of interactions.

## Supported Features
1. Hunting
- Encounters Pokémon and uses a ball depending on the rarity of the Pokémon.
- Stops if a captcha appears and automatically continues after the captcha is solved.

2. Fishing
- Spawns a fish, pulls the fishing rod and uses a ball depending on the rarity of the Pokémon.
- It has the data for every fish's rarity, so it knows the rarity even though Pokémeow doesn't show it.

3. Captcha Solver
- Automatically solves captcha.
- Retries if incorrect upto 3 retries (total 4 attempts).

4. Auto Buy Balls
- Buys balls automatically when you run out of them (works with both hunting and fishing)!
- Number of balls to buy can be specified in `config.json`.

5. Multiple Accounts
- You can run multiple accounts at once!

## Upcoming Features
1. Logging Tables
- Format logs in tables for multiple accounts.

## Config
```json
{
    "Clients": [
        {
            "Token": "", // Your discord token
            "ChannelID": "", // Channel ID for hunting
            "FishChannelID": "", // Channel ID for fishing
            "Hunting": true, // Disable/Enable Hunting
            "Fishing": true, // Disable/Enable Fishing
            "Balls": {
                "Common": "pb",
                "Uncommon": "pb",
                "Rare": "gb",
                "Super Rare": "ub",
                "Legendary": "mb",
                "Shiny": "mb",
                "Shiny Event": "mb",
                "Shiny Full-odds": "prb"
            }, // Which ball to use for which rarity during hunting
            "FishBalls": {
                "Common": "pb",
                "Uncommon": "gb",
                "Rare": "ub",
                "Super Rare": "ub",
                "Legendary": "db",
                "Shiny": "mb",
                "Shiny Event": "mb",
                "Shiny Full-odds": "prb"
            }, // Which ball to use for which rarity during fishing
            "AutoBuy": {
                "pb": 50,
                "gb": 25,
                "ub": 5,
                "mb": 1
            } // How many balls to auto-buy when you have 0 left.
        }
        // You can add more clients after this with the same type of config as above
    ]
}
```
- Use different channels for each account.
- Hunting and fishing for different accounts can be in the same server.
- The Hunting and Fishing channels for the same account must be in different servers/guilds.
- Please try grinding in servers with only PokeMeow bot and without any other bots if you face issues.

## Get Token ?

<strong>Run code (Discord Console - [Ctrl + Shift + I])</strong>

```js
window.webpackChunkdiscord_app.push([
  [Math.random()],
  {},
  req => {
    for (const m of Object.keys(req.c)
      .map(x => req.c[x].exports)
      .filter(x => x)) {
      if (m.default && m.default.getToken !== undefined) {
        return copy(m.default.getToken());
      }
      if (m.getToken !== undefined) {
        return copy(m.getToken());
      }
    }
  },
]);
console.log('%cWorked!', 'font-size: 50px');
console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
```

## Requirements
- Requires Python 3.8+ to be installed.
- Requires FastAPI, Uvicorn and Ultralytics to be installed :-
  - `pip install fastapi`
  - `pip install "uvicorn[standard]"`
  - `pip install ultralytics`

## Launching
1. ##### Captcha Solver
- Download the `Solver1850.pt` file from releases.
- Download the `CaptchaSolver.py` file from the repository.
- Place the above two files in the same folder.
- Run the command `uvicorn CaptchaSolver:app --reload` in the terminal while in that folder.

2. ##### Grinder
- Download the `config.json` file and the `fishes.json` file.
- Download the executable file for your operating system from the release tab.
- The `config.json`, `fishes.json` and the executable must be in the same folder.
- Run the executable, and the grinder should start.

## Stopping
To stop the program simply close the command prompt or press CTRL+C in the command prompt.

## Disclaimer ⚠️
- I am of course not responsible for any ban you receive for using this bot.
- Please keep an eye on the bot. Do not be irresponsible if you don't want to get banned.
- Please do not grind on public servers.
