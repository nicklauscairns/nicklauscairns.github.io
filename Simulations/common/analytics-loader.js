(function() {
  if (window.__simAnalyticsInitialized) return;
  window.__simAnalyticsInitialized = true;

  const GA_TRACKING_ID = 'G-DKDGNLCXQ1';

  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function(){ window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', GA_TRACKING_ID);

  const src = `https://www.googletagmanager.com/gtag/js?id=${GA_TRACKING_ID}`;
  if (!document.querySelector(`script[src="${src}"]`)) {
    const script = document.createElement('script');
    script.async = true;
    script.src = src;
    document.head.appendChild(script);
  }
})();
