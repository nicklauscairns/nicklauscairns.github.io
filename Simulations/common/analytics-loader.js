(function() {
  const GA_TRACKING_ID = 'G-DKDGNLCXQ1';

  // Define dataLayer and gtag function
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', GA_TRACKING_ID);

  // Create and inject the gtag.js script
  var script = document.createElement('script');
  script.async = true;
  script.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_TRACKING_ID;
  document.head.appendChild(script);
})();
