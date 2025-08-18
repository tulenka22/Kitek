export function createLink(url, title) {
  return { url, title }
}

export function createColumn(title, ...links) {
  return { title, links }
}
