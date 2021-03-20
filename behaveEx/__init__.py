"""
pip install behave

[project root directory]
|‐‐ [product code packages]
|-- features
|   |-- environment.py
|   |-- *.feature
|   `-- steps
|       `-- *_steps.py
`-- [behave.ini|.behaverc|tox.ini|setup.cfg]

# Run all scenarios in the project
behave

# Run all scenarios in a specific feature file
behave features/web.feature

# Filter tests by tag
behave --tags-help
behave --tags @duckduckgo
behave --tags ~@unit
behave --tags @basket --tags @add,@remove

# Write a JUnit report (useful for Jenkins and other CI tools)
behave --junit

# Don't print skipped scenarios
behave -k

"""