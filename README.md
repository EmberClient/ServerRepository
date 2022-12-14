# Server Repository

The Server Repository is a list of information about Minecraft Servers to allow enriching information to be displayed while using Ember Client.

## Adding Your Server

If you would like to add your server to the list, you will need to create a pull request that contains your server's information in a valid JSON format.

### Step 1: Fork the Repository

First, you will need to fork this repository so you have your own copy of it. To do this, click the “Fork” button in the top right corner of the page. This will create a copy of the repository under your own GitHub account.

### Step 2: Create a JSON File

Once you have your own copy of the repository, you will need to create a new file containing your server's information in valid JSON format. This file should be named after your server and should be placed in the `/servers` directory.

The JSON file should contain a key/value pair for each field that is needed for your server, such as name, any applicable IP address' or domain names, types, versions, etc. For example, a file for our test server might look like this:

```json
{
  "name": "Server Name",
  "hosts": ["ip.address"],
  "versions": ["supported.version"],
  "primaryColour": "#FFFFFF",
  "type": ["Vanilla"]
}
```

Please keep in mind that a single host will match all subdomains, so there's no need to add any additional hosts for regional proxies.

### Step 3: Commit and Push Your Changes

Once you have created your JSON file, you will need to commit and push your changes to GitHub. To do this, use either the GitHub Desktop application or the command line. If you are using GitHub Desktop, simply select “Commit and Push” when you have finished making changes. If you are using the command line, type `git add <filename>` to add the file and `git commit -m "<message>"` to commit your changes locally. Finally, type `git push` to push your changes up to GitHub.

### Step 4: Create a Pull Request

Now that your changes have been pushed up to GitHub, you can create a pull request to add your server to the list. To do this, go back to the main page of this repository (the one under Ember Client's account) and click on “Pull Requests” in the top menu bar. Then, click “New Pull Request” and select your fork from the “compare” dropdown menu. Finally, enter a summary of your changes in the comment box and click “Create Pull Request”.

Your pull request will then be reviewed by one of our maintainers and merged into the main repository if it is approved!

## Supported Types

We support various different Minecraft versions and server types, a list of which can be found below:

### Server Types

- Vanilla
- Minigames
- Skyblock
- Survival
- Creative
- PvP
- Prison
- Factions

### Minecraft Versions

- 1.7
- 1.8
- 1.12
- 1.19

## FAQ

### Can I use this for my own project?

Yes, you can use data from this repository for your own project as long as you follow the license terms.

### Can I add my server to the list?

Yes, you can add your server to the list by following the steps above.

### I can't find a type that matches my server, what should I do?

If you can't find a type that matches your server, you can create a pull request to add a new type to the list. If you do this, please make sure that you add the type to the list in the README.MD file. If you are unsure about what to add, you can create an issue and we will add it for you.
