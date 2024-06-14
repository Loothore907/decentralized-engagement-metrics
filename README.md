## Introduction:

We begin our journey with the basic thesis that community engagement creates substantial value for any project. In today's world, social media engagement can make or break a project. Benefits and value are amplified through social media onboarding, while FUD and other negative social metrics can tank a growing project before it ever gets its feet off the ground.

This relationship can be adversarial: projects need active communities to grow but fear the oversight and negative consequences that come from ignoring their feedback and guidance. As a result, many projects hamper their own growth by limiting the range and scope of their community, opting instead for the easier route of VCs and large wallet investors.

The Decentralized Engagement Metrics (DEM) module aims to incentivize substantive community engagement through the 'Twitter' (X) app by tracking and rewarding community engagement with Engagement Value (EV) points. We will then convert that value into a tokenized governance enhancement vehicle.

Vision
In the ever-expanding world of cryptocurrency and blockchain, understanding social interactions and engagement is crucial for effective governance and community building. DEM's vision is to create a detailed and granular map of social media interactions, enabling projects to make informed decisions based on genuine community engagement.

Goals
Tokenization of Engagement: Transform engagement metrics into tokenized assets, empowering projects to integrate social media activity directly into their governance or points systems.
Decentralized Data Storage: Store our growing vector database on a decentralized platform, ensuring accessibility and transparency for all stakeholders.
Interoperability: Design DEM to be used by various projects and protocols, fostering collaboration and enhancing the overall ecosystem.

Engagement

Data Collection
Our Engagement Module will extract posts, replies, and additional metadata from ecosystem and participating community accounts. All contextually relevant content will be saved in a vector database for later analysis. Tags, mentions, and quotes will also be tracked independently of account tracking. Any post or reply with a contextually relevant tag, mention, or quote will also be saved within our database. These will then be cross-referenced with participating accounts, and rewards will be assigned accordingly.

Engagement Rewards
Project/Ecosystem Accounts: Engagement rewards for these accounts will be consolidated into one wallet. These are the only ENG rewards that will be delegatable, allowing the team to allocate engagement rewards to community wallets to reward ecosystem value not covered in either our enhancement system or the project's existing governance system.

Community Accounts: Engagement rewards for community accounts will be dropped into their linked governance wallet. These tokens will NOT be transferable outside the governance staking UI. When you log into your project's governance UI, you will be prompted to stake all available ENG tokens. The staked ENG tokens will exist alongside your existing governance stake, with a UI toggle to apply your ENG value to either governance or rewards.

Note: This module is designed to enhance the "Active Stake Weighted Governance" model, allowing the toggle to be switched at any time without negative outcomes. For other governance systems, a six-month cooldown on the governance toggle is recommended to prevent manipulation.

Why DEM?
The primary challenge in governance systems is the accurate assessment of community sentiment and engagement. Traditional methods often fall short due to their centralized nature and susceptibility to manipulation. DEM leverages the transparency and security of blockchain technology to provide a decentralized solution that benefits all stakeholders. By integrating social media metrics into governance, projects can ensure that their decisions reflect the genuine interests and activity of their community members.

Getting Started
This repository, when complete, will provide all the tools needed to collect, analyze, and reward Twitter (X) engagement. All our training data and model weights will also be included. Ideally, our Llama 3 model and our vector database will be available on decentralized storage platforms.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)
- [Acknowledgements](#acknowledgements)

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/engagement_module.git
    cd engagement_module
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory and add your Twitter API credentials:

      ```
      API_KEY=your_api_key
      API_SECRET_KEY=your_api_secret_key
      ACCESS_TOKEN=your_access_token
      ACCESS_TOKEN_SECRET=your_access_token_secret
      ```

5. Ensure your `twitter_accounts.csv` file is populated with the Twitter accounts you want to monitor:

    ```csv
    username
    @emfr2u
    @wenwencoin
    ```

## Usage

### Fetching Twitter Data

To fetch the latest tweets and responses, run:

```bash
python fetch/fetch_twitter_data.py
python fetch/fetch_general_tweets.py
```


### Running the Entire Workflow

To execute the complete workflow, run:

```bash
python workflow.py
```

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact Information

- **Twitter**: [@emfr2u](https://twitter.com/emfr2u)
- **Discord**: loothore (loot)
- **Medium**: [Loothore907](https://medium.com/@Loothore907)

## Acknowledgements

- Special thanks to the Jupiter DAO community for their support.
- [Unsloth](https://www.unsloth.com) for their helpful tools.
- [Hugging Face](https://huggingface.co) for providing excellent AI models.
