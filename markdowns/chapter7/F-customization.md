# Customization

When R starts it executes the function `.First` in `~/.Rprofile` (if it exists).
Similarly, R executes the function `.Last` in the same file at the end of any R.
Here's an example of how to customize your R environment:

@[]({"project": "R", "stubs": ["chapter7/pi.R", "chapter7/.Rprofile"], "command": "chapter7/customization.sh"})
