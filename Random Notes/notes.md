## Zshenv vs Zprofile vs Zshrc

- .zshenv - always sourced - $PATH : exported variables and path available to all programs
- .zprofile - login shells
- .zshrc - for interactive shells (Shell you interact with)

### Path

- Contain variables for all environment running programs to access (hold sbin and bin directories)
- env variables are prefixed with $
- printenv prints all the environment variables
- aliases can be used to set command line commands
    - Command line variables - brew
    - PATH / Environment variables - THIS_IS_MY_PATH => Key Value pair where value normally path to a file or .exe program


### Types of shell

- bash (Unix)
- zsh (Mac)