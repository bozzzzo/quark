# Examples

This directory contains example Quark code.


## Slack

The bot connects to Slack as you and monitors every message you receive (except from Slack integrations or from itself). If it sees a message containing the trigger text, it echoes that message back on the same channel.

Avoid running multiple bots simultaneously. The Python bot censors itself, but the JS and Java bots may trigger one another, causing a loop that will lead to your connections getting dropped.


### Prerequisites

Log into Slack, then grab an API token from https://api.slack.com/web#authentication

Store that token in a file

    echo 'your API token here' > slack-bot/.slack.token


### Python

**Note**: [This will require twisted.](http://datawire.github.io/quark/install/install.html#python-requirements>)

Compile the quark interface into a package. Install the quark twisted
integration and the generated package:

    quark --python package slack.q
    pip install --user datawire-quark-twisted slack/py/dist/slack-0.1.0-py2-none-any.whl

**Note**: if you are testing quark inside a virtualenv you should drop the `--user` flag for `pip install`

Run the bot

    slack-bot && python bot.py

TODO: move this to troubleshooting in the docs and somehow link from here.
**Note**: in case running the bot produces a `UserWarning: You do not have a working installation of the service_identity module: 'No module named pyasn1.codec.der.decoder'` you can usually fix that with a `pip uninstall service_identity && pip install --user service_identity`

### JavaScript

**Note**: [This will require node 4.2.2 or later.](http://datawire.github.io/quark/install/install.html#javascript-requirements>)

Compile the quark interface into a package. Install that package.

    quark --javascript package slack.q
    npm install datawire-quark-node slack/js/slack.tgz

Run the bot

    cd slack-bot && node bot.js


### Java

**Note**: This will require maven.

Compile the quark interface. Install the result using Maven.

    quark --java compile slack.q && ( cd slack/java && mvn install; )


Build and run the bot

    cd slack-bot && mvn compile && mvn exec:java -Dexec.mainClass="bot.SlackBot"
