import os
import json
import frontmatter

# Define the directory containing the markdown files
blogs_directory = '/home/vast/repos/LearnWithMe/Learnings'
output_file_path = '/home/vast/repos/gaurav8341.github.io/frontend/public/blogs.json'

# List to hold blog entries
blogs = []

# Iterate over all markdown files in the directory
for filename in os.listdir(blogs_directory):
    if filename.endswith('.md'):
        file_path = os.path.join(blogs_directory, filename)
        
        # Read the markdown file
        with open(file_path, 'r') as file:
            post = frontmatter.load(file)
            content = post.content
            
            # Extract details from the front matter and content
            slug = os.path.splitext(filename)[0]
            title = post.get('title', 'Untitled')
            date = post.get('date', 'Unknown date')
            tags = post.get('tags', [])
            preview = content[:100] + '...' if len(content) > 100 else content
            
            # Create a blog entry
            blog_entry = {
                'slug': slug,
                'title': title,
                'path': f'{file_path}',
                'date': date,
                'tags': tags,
                'preview': preview
            }
            
            # Add the blog entry to the list
            blogs.append(blog_entry)

# Write the blogs list to the output JSON file
with open(output_file_path, 'w') as output_file:
    json.dump(blogs, output_file, indent=2)

print('blogs.json generated successfully.')
