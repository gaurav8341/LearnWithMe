# LearnWithMe
My Knowledge base

Learnings: will have my knowldge base through short form content.
deepdive: Will have long deepdive into any specific subject.
Notes: will have references, links, urls for blog or any tool. 

To generate the mermaid graph in pandoc files

```sh
PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome pandoc
     ~/repos/LearnWithMe/Learnings/oauth-post.md -o ~/oauth.docx
     --filter=mermaid-filter
```