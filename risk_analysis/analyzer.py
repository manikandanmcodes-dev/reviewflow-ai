def analyze_risks(files):

    risks = []

    for file in files:

        patch = file.get("patch")

        if not patch:
            continue

        if "print(" in patch:
            risks.append({
                "file": file["filename"],
                "risk": "Debug print statement found"
            })

        if "TODO" in patch:
            risks.append({
                "file": file["filename"],
                "risk": "TODO found"
            })

        if "FIXME" in patch:
            risks.append({
                "file": file["filename"],
                "risk": "FIXME found"
            })

    return risks