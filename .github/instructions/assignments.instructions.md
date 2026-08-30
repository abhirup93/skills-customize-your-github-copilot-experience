---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files should follow these guidelines to maintain consistency and provide a high-quality learning experience for students.

## 1. Template Usage

- Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../templates/assignment-template.md).
- The assignment must be created as a `README.md` file
- Do not remove or skip required sections from the template.

## 2. Folder Structure

- Each assignment must have its own dedicated subfolder under [`assignments/`](../../assignments/)
- Folder names should be descriptive and use lowercase with hyphens (e.g., `python-basics`, `data-analysis`)
- Include `README.md` as the main assignment file
- Include supporting files such as `starter-code.py`, `data.csv`, etc., in the same folder

## 3. Project Standards & Educational Guidelines

Follow the project's educational standards when creating assignments:

- **Learning-focused**: Design assignments with clear, achievable learning objectives that build on core concepts
- **Student-friendly**: Use encouraging language and clear explanations that motivate students
- **Consistent styling**: Maintain visual consistency with existing assignments, including emoji usage in headers
- **Organized structure**: Keep all assignment materials clearly organized and easy to navigate

## 4. Section Guidance

The section headers should reflect the structure in the template, including the exact icon usage (📘, 🎯, 📝, 🛠️).

### Title (📘 Assignment: [Title])
- Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`)
- Use title case for assignment names

### Objective (🎯 Objective)
- Write 1-2 sentences summarizing what the student will learn or accomplish
- Focus on the main skills or concepts students will develop
- Use student-friendly language that motivates learning

### Tasks (📝 Tasks)
For each task, follow this structure:

#### Task Title (🛠️ [Task Title])
- Use a specific, action-oriented task name
- Keep task names concise and descriptive

#### Description
- Clearly state what the student must do
- Explain the purpose and context of the task
- Use simple, direct language

#### Requirements
- Use bullet points to list specific, measurable expected outcomes
- Be specific about deliverables and features
- Provide example input/output in code blocks when helpful
- Include format: "Completed program should:"

## 5. Best Practices

- **Keep assignments concise**: Focus on core concepts without overwhelming students
- **Provide examples**: Include clear example usage or expected output
- **Build progressively**: Structure tasks from simpler to more complex
- **Use consistent formatting**: Follow markdown conventions and maintain visual hierarchy
- **Encourage learning**: Write in a supportive, motivational tone

Do not include extra sections unless explicitly specified.