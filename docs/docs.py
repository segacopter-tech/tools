# regular docs generator for segcopter tech project docs

generated_docs = []

print("we are gonna generate some docs starters in markdown for you be done soon.")

generated_docs.append("# docs")
generated_docs.append("## about")
generated_docs.append("text info about your project")
generated_docs.append("## copyright")
generated_docs.append("copyright info like the license")
generated_docs.append("## dependencies")
generated_docs.append("dependencies for your project")
generated_docs.append("## install")
generated_docs.append("how to install your project")

with open("output_docs.md", "w") as file:
    for item in generated_docs:
        file.write(f"{item}\n")

print("finished!")
