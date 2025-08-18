export function isMobile() {
  const userAgent = process.server
    ? context.req.headers['user-agent'] || 'default'
    : navigator.userAgent
  const isMobile =
    /Mobile|webOS|BlackBerry|IEMobile|MeeGo|mini|Fennec|Windows Phone|Android|iP(ad|od|hone)/i.test(
      userAgent
    )
  return isMobile
}
