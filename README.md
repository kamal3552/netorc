<h1 align="center">
    <img alt="netorc logo" src="https://avatars.githubusercontent.com/u/130744316?s=200&v=4" width="200"/><br>NetORC
</h1>

<p align="center">NetORC lays the foundation for central network orchestration. It acts as an intermediary between your business support systems and the network automation tooling of your choice. By being tool agnostic, the project aims to enhance the adoption of network automation into other business functions through its simple-to-use API.</p>


## Project Goals

- Develop an open-source, vendor-agnostic network orchestrator API.
- Prioritize reliability and usability over speed.
- Provide a set of helpful add-ons to support the adoption of central orchestration.
- Enable queuing and feedback of job progress.

## Founding Principles

- The orchestrator should lay the foundations for bespoke customization and improvement, rather than trying to be exhaustive.

## Demo Quick Start

First, [download](https://docs.docker.com/get-docker/) and install 🐳**Docker**. Engine version: 19.03.0 or higher is required.

Next, clone the respository using the following command: 
```bash
git clone https://github.com/netorc-community/netorc.git && cd netorc
```

Finally, build the images and start the containers with:
```bash
docker compose -f docker-compose.dev.yml
```

Navigate to `localhost:8000/api", congrats! 🎉. Documentation can be found at /docs