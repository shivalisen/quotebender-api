# Quotebender API

A REST API for quotes from Avatar: The Last Airbender.

---

## Features

- Filter quotes by character, season number, episode number, or all 3
- Get a random quote

---

## API Endpoints

Base URL: WIP

| Method | Endpoint                  | Description                            |
|--------|---------------------------|----------------------------------------|
| GET    | `/quotes`                 | Get all quotes                         |                   |
| GET    | `/quotes?character=iroh`  | Get quotes filtered by character name |
| GET    | `/quotes?season=1`  | Get quotes filtered by season |
| GET    | `/quotes?season=3&episode=9`  | Get quotes filtered by episode |
| GET    | `/quotes/random`          | Get a random quote  

Example JSON response:

```json
{
  "quote": "Sometimes, life is like this dark tunnel. You can't always see the light at the end of the tunnel, but if you just keep moving, you will come to a better place.",
  "character": "Iroh",
  "episode_name": "The Crossroads of Destiny",
  "season_number": 2,
  "episode_number": 20
}
