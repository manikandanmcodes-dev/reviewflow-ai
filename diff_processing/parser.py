def process_files(files):

    results = []

    for file in files:

        filename = file["filename"]

        if filename.endswith(".py"):
            file_type = "Python"

        elif filename.endswith(".js"):
            file_type = "JavaScript"

        elif filename.endswith(".md"):
            file_type = "Documentation"

        else:
            file_type = "Other"

        results.append({
            "filename": filename,
            "type": file_type,
            "additions": file["additions"],
            "deletions": file["deletions"]
        })

    return results