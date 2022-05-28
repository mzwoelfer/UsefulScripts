<%* 
const title = tp.file.title
if (title.startsWith("@")) {
	await tp.file.move("/People/" + title)
	return tp.file.include('[[People (Template)]]')
} else {
	return tp.file.include('[[Starter Note (Template)]]')
}
%>