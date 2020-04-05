hljs.registerLanguage('tree', () => {
  return {
    case_insensitive: true,
    contains: [
      {
        className: 'string',
        begin: '^[A-Za-z0-9 \_\-]+$',
      },
      {
        className: 'string',
        begin: '[A-Za-z0-9 \_\-]+/$',
      },
      {
        className: 'number',
        begin: '[A-Za-z0-9 \_\-]+\.(jpg|png|gif|tiff|mp4|mp3)$',
      }
    ]
  };
});
