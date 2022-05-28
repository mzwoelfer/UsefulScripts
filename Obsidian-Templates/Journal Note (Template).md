<% tp.file.include('[[Frontmatter (Template)]]') %>
<% await tp.file.move("/Journal/" + tp.file.title) %>


# <% tp.file.creation_date("DD.MM.YYYY")%>

<% tp.file.cursor(1) %>




---


## 📇 Additional Metadata

- 🗓️ Week:: [[<% moment(tp.file.title).format("[W]ww-YYYY") %>]]

- 🗂 Type:: #type/journal