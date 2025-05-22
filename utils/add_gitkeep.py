import os

def add_gitkeep_to_empty_student_folders(root_dir):
    """
    Recursively find student folders (W*/g*/*) and add a .gitkeep file if folder is empty.
    """

    for week_name in os.listdir(root_dir):
        week_path = os.path.join(root_dir, week_name)
        if not os.path.isdir(week_path) or not week_name.lower().startswith('w'):
            continue  # Skip non-week folders

        for group_name in os.listdir(week_path):
            group_path = os.path.join(week_path, group_name)
            if not os.path.isdir(group_path) or not group_name.lower().startswith('g'):
                continue  # Skip non-group folders

            for student_folder in os.listdir(group_path):
                student_path = os.path.join(group_path, student_folder)
                if not os.path.isdir(student_path):
                    continue  # Not a folder, skip

                # Check if folder is empty
                if not os.listdir(student_path):
                    gitkeep_path = os.path.join(student_path, '.gitkeep')
                    with open(gitkeep_path, 'w') as f:
                        pass  # Create empty .gitkeep file
                    print(f"Added .gitkeep to empty folder: {student_path}")


if __name__ == "__main__":
    # Change this to your root assignment folder path
    assignment_root = "./"  # or e.g. "/path/to/classroom_repo"

    add_gitkeep_to_empty_student_folders(assignment_root)
