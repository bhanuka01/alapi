# AL API

This repository hosts the JSON data for the AL Past Paper Flutter app. The data is organized by year, exam type (A/L and O/L), and subject stream.

## Download the App

[<img src="https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png" alt="Get it on Google Play" height="80">](https://play.google.com/store/apps/details?id=com.bhanu.sriexam&pli=1)

## API Structure

The API is file-based, and the data is served directly from this GitHub repository. The base URL for accessing the files is:

```
https://raw.githubusercontent.com/bhanuka01/alapi/main/
```

### Directory Structure

The data is organized into the following main directories:

- `25al/`: Contains the data for the G.C.E. Advanced Level (A/L) examination.
- `25ol/`: Contains the data for the G.C.E. Ordinary Level (O/L) examination.
- `image/`: Contains images used in the app.

### Accessing Data

To access the data, you append the path to the desired JSON file to the base URL.

#### Example: Accessing the main A/L data

To get the list of available streams for the A/L exam, you would access the `25al/home.json` file:

```
https://raw.githubusercontent.com/bhanuka01/alapi/main/25al/home.json
```

The response will be a JSON object containing a list of streams, like this:

```json
{
    "data": [
        {
            "title": "A/L",
            "subtitle": "",
            "head": "Math Stream",
            "body": "2",
            "url": "https://raw.githubusercontent.com/bhanuka01/alapi/main/25al/stream/mathsstream.json",
            "img": "https://i.pinimg.com/736x/ac/c9/7c/acc97c4f6ba2fc68266b7e687511abca.jpg"
        },
        {
            "title": "",
            "subtitle": "",
            "head": "Biology Stream",
            "body": "2",
            "url": "https://raw.githubusercontent.com/bhanuka01/alapi/main/25al/stream/biostream.json",
            "img": "https://raw.githubusercontent.com/bhanuka01/pothlanthaya/main/couragedisliked/img.jpg"
        },
        {
            "title": "",
            "subtitle": "",
            "head": "Commerce Stream",
            "body": "2",
            "url": "https://raw.githubusercontent.com/bhanuka01/alapi/main/25al/stream/commstream.json",
            "img": "https://raw.githubusercontent.com/bhanuka01/pothlanthaya/main/couragedisliked/img.jpg"
        },
        {
            "title": "",
            "subtitle": "",
            "head": "Technology Stream",
            "body": "1",
            "url": "https://raw.githubusercontent.com/bhanuka01/alapi/main/25al/stream/techstream.json",
            "img": "https://raw.githubusercontent.com/bhanuka01/pothlanthaya/main/couragedisliked/img.jpg"
        }
    ]
}
```

Each object in the `data` array contains a `url` field that points to the JSON file for that specific stream. You can then use this URL to get the subjects within that stream.

### O/L Data

Similarly, you can access the O/L data by using the `25ol/` directory. For example, to get the list of subjects for the O/L exam, you would use:

```
https://raw.githubusercontent.com/bhanuka01/alapi/main/25ol/home.json
```

This will provide a list of subjects and URLs to access the papers for each subject.
