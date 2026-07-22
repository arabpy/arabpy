import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docsSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      collapsible: true,
      collapsed: false,
      items: [
        'introduction',
        'installation',
        'quick-start',
        'why-arabpy',
      ],
    },
    {
      type: 'category',
      label: 'Arabic Syntax',
      collapsible: true,
      collapsed: false,
      items: [
        'arabic-syntax/index',
        'arabic-syntax/keywords',
        'arabic-syntax/built-in-functions',
        'arabic-syntax/modules',
      ],
    },
    {
      type: 'category',
      label: 'API Reference',
      collapsible: true,
      collapsed: false,
      items: [
        'api/index',
        'api/translator',
        'api/runner',
        'api/dictionary',
      ],
    },
    {
      type: 'category',
      label: 'Examples',
      collapsible: true,
      collapsed: false,
      items: [
        'examples/index',
        'examples/variables',
        'examples/functions',
        'examples/classes',
        'examples/loops',
        'examples/conditions',
        'examples/lists',
        'examples/dictionaries',
        'examples/exceptions',
        'examples/file-handling',
        'examples/oop',
        'examples/decorators',
        'examples/generators',
        'examples/context-managers',
        'examples/async-await',
        'examples/dataclasses',
        'examples/typing',
      ],
    },
    {
      type: 'category',
      label: 'Community',
      collapsible: true,
      collapsed: false,
      items: [
        'faq',
        'contributing',
        'roadmap',
        'changelog',
        'license',
      ],
    },
  ],
};

export default sidebars;
