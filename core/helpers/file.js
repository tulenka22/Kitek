export function loadDynamic(filePath) {
  return new Promise((resolve, reject) => {
    let xhr = new XMLHttpRequest()
    // TODO: REMOVE IT!
    xhr.open('get', `/${filePath}`)
    xhr.send()
    xhr.onload = () => resolve(xhr.response)
    xhr.onerror = () => reject(xhr)
  })
}
