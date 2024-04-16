# `developersIndia` resources

> The developersIndia Host for some cool & useful resources to learn new things in tech.

[![Discord](https://img.shields.io/discord/669880381649977354?color=%237289da&label=Discord&logo=Discord)](https://discordapp.com/invite/MKXMSNC)
[![Subreddit subscribers](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdevelopersindia.github.io%2Fmetrics%2Fdata%2F&query=%24.totalMembers&suffix=%20members&style=flat&logo=reddit&label=r%2FdevelopersIndia&color=orange&link=https%3A%2F%2Fwww.reddit.com%2Fr%2FdevelopersIndia
)](https://www.reddit.com/r/developersIndia/)

# 👀 How does this project work?

The resources repository acts as a "static datastore" for our [**saadhan project**](https://saadhan.developersindia.in/). Here is a brief overview:
1. You contribute resources here, by updating the correct `index.json`.
2. Your PR gets reviewed & merged.
3. The new/updated resource is now visible on the saadhan website.

## 🤨 What's a "static datastore"
- Its a collection of JSON files, like literally.
- GitHub returns JSON files as JSON, if they are named as `index.json` and are placed in a directory. This gives us the leverage to use the [`resources` github pages site](https://developersindia.github.io/resources/) as an API for the saadhan website. <br>
  Here is a sample endpoint for DSA resources demonstrating the static API
  ```
  https://developersindia.github.io/resources/dsa/index.json
  ```

## 🙌🏽 Organised resources with [JSON Schema](https://json-schema.org/)
- We don't like big readme files with a collection of links (see for yourself how [horrible this looks 🤮](https://github.com/developersIndia/resources/blob/099258bb6daffd67475add7e8ef137b430c50c33/README.md)).
- To make the experience better we utilise JSON Schemas which provides a validation layer on top your JSON data.
- This is how the [`resources` schema looks like](https://github.com/developersIndia/resources/blob/master/resource.schema)

# 📜 License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

# 👋 Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines for the process of submitting pull requests to us.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://nuhman.github.io"><img src="https://avatars3.githubusercontent.com/u/15177381?v=4?s=100" width="100px;" alt="Muhammed Nuhman"/><br /><sub><b>Muhammed Nuhman</b></sub></a><br /><a href="#content-nuhman" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sbmthakur"><img src="https://avatars2.githubusercontent.com/u/7949156?v=4?s=100" width="100px;" alt="Shubham Thakur"/><br /><sub><b>Shubham Thakur</b></sub></a><br /><a href="#content-sbmthakur" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SharmaAayush"><img src="https://avatars.githubusercontent.com/u/29497880?v=4?s=100" width="100px;" alt="Ayush Sharma"/><br /><sub><b>Ayush Sharma</b></sub></a><br /><a href="#content-SharmaAayush" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/BlackGoku36"><img src="https://avatars.githubusercontent.com/u/36535717?v=4?s=100" width="100px;" alt="Urjasvi Suthar"/><br /><sub><b>Urjasvi Suthar</b></sub></a><br /><a href="#content-BlackGoku36" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://jarmos.netlify.app/"><img src="https://avatars.githubusercontent.com/u/31373860?v=4?s=100" width="100px;" alt="Somraj Saha"/><br /><sub><b>Somraj Saha</b></sub></a><br /><a href="#content-Jarmos-san" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://bhupeshpradhan.vercel.app/"><img src="https://avatars.githubusercontent.com/u/76522149?v=4?s=100" width="100px;" alt="Bhupesh Pradhan"/><br /><sub><b>Bhupesh Pradhan</b></sub></a><br /><a href="#infra-HanakoK9" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/V3dantSh4rma"><img src="https://avatars.githubusercontent.com/u/70263758?v=4?s=100" width="100px;" alt="Vedant Sharma"/><br /><sub><b>Vedant Sharma</b></sub></a><br /><a href="#content-V3dantSh4rma" title="Content">🖋</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://tailwind-nextjs-portfolio.vercel.app/"><img src="https://avatars.githubusercontent.com/u/18483618?v=4?s=100" width="100px;" alt="Manav-SM"/><br /><sub><b>Manav-SM</b></sub></a><br /><a href="#content-Manav-SM" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SameerSahu007"><img src="https://avatars.githubusercontent.com/u/29480670?v=4?s=100" width="100px;" alt="Sameer Sahu"/><br /><sub><b>Sameer Sahu</b></sub></a><br /><a href="#content-SameerSahu007" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://dev.to/delta456"><img src="https://avatars.githubusercontent.com/u/28479139?v=4?s=100" width="100px;" alt="Swastik Baranwal"/><br /><sub><b>Swastik Baranwal</b></sub></a><br /><a href="#content-Delta456" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yaswanth-vakkala"><img src="https://avatars.githubusercontent.com/u/100300292?v=4?s=100" width="100px;" alt="yaswanth v"/><br /><sub><b>yaswanth v</b></sub></a><br /><a href="#content-yaswanth-vakkala" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://animesh-ghosh.github.io/"><img src="https://avatars.githubusercontent.com/u/34956994?v=4?s=100" width="100px;" alt="MaDDogx"/><br /><sub><b>MaDDogx</b></sub></a><br /><a href="#content-Animesh-Ghosh" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://akshat.shastraos.co/"><img src="https://avatars.githubusercontent.com/u/69577224?v=4?s=100" width="100px;" alt="Akshat Sharma"/><br /><sub><b>Akshat Sharma</b></sub></a><br /><a href="#content-akshatcoder-hash" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://spookyintheam.codes"><img src="https://avatars.githubusercontent.com/u/68803793?v=4?s=100" width="100px;" alt="spooky"/><br /><sub><b>spooky</b></sub></a><br /><a href="#content-ghostx31" title="Content">🖋</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/HarshitJoshi9152"><img src="https://avatars.githubusercontent.com/u/37842304?v=4?s=100" width="100px;" alt="Harshit"/><br /><sub><b>Harshit</b></sub></a><br /><a href="#content-HarshitJoshi9152" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://gsolanki.vercel.app"><img src="https://avatars.githubusercontent.com/u/34185908?v=4?s=100" width="100px;" alt="Solanki Gaurav"/><br /><sub><b>Solanki Gaurav</b></sub></a><br /><a href="#content-gau2107" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/triach-rold"><img src="https://avatars.githubusercontent.com/u/156170660?v=4?s=100" width="100px;" alt="Triach Rold"/><br /><sub><b>Triach Rold</b></sub></a><br /><a href="#content-triach-rold" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LinearArray"><img src="https://i.imgur.com/HADyaIG.jpeg" width="100px;" alt="LinearArray"/><br /><sub><b>LinearArray</b></sub></a><br /><a href="#content-lineararray" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/yashasnadigsyn"><img src="https://avatars.githubusercontent.com/u/103478177?v=4?s=100" width="100px;" alt="Yashas Nadig"/><br /><sub><b>Yashas Nadig</b></sub></a><br /><a href="#content-yashasnadigsyn" title="Content">🖋</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
