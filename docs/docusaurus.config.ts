import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import { themes as prismThemes } from 'prism-react-renderer';

const config: Config = {
  title: 'ArabPy',
  tagline: 'Write Python in Arabic',
  favicon: 'img/favicon.ico',

  url: 'https://arabpy.github.io',
  baseUrl: '/',
  organizationName: 'arabpy',
  projectName: 'arabpy',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  onBrokenAnchors: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.ts'),
          editUrl: 'https://github.com/arabpy/arabpy/edit/main/docs/',
          versions: {
            current: {
              label: '1.0.0',
              path: '/',
            },
          },
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'ArabPy',
      logo: {
        alt: 'ArabPy Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'docsSidebar',
          position: 'left',
          label: 'Documentation',
        },
        {
          type: 'doc',
          docId: 'api/index',
          position: 'left',
          label: 'API Reference',
        },
        {
          type: 'doc',
          docId: 'examples/index',
          position: 'left',
          label: 'Examples',
        },
        {
          href: 'https://github.com/arabpy/arabpy',
          label: 'GitHub',
          position: 'right',
        },
        {
          href: 'https://pypi.org/project/arabpy/',
          label: 'PyPI',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Documentation',
          items: [
            {
              label: 'Getting Started',
              to: '/docs/introduction',
            },
            {
              label: 'API Reference',
              to: '/docs/api/index',
            },
            {
              label: 'Examples',
              to: '/docs/examples/index',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/arabpy/arabpy',
            },
            {
              label: 'Issues',
              href: 'https://github.com/arabpy/arabpy/issues',
            },
            {
              label: 'Contributing',
              to: '/docs/contributing',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'PyPI',
              href: 'https://pypi.org/project/arabpy/',
            },
            {
              label: 'License',
              to: '/docs/license',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} ArabPy. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python', 'bash'],
    },
    announcementBar: {
      id: 'announcement',
      content: '🎉 ArabPy 1.0.0 is now available! <a href="/docs/changelog">See what\'s new</a>',
      backgroundColor: '#16a34a',
      textColor: '#ffffff',
      isCloseable: true,
    },
  } satisfies Preset.ThemeConfig,

  plugins: [
    [
      require.resolve('@docusaurus/plugin-client-redirects'),
      {
        redirects: [
          {
            from: '/docs',
            to: '/docs/introduction',
          },
        ],
      },
    ],
  ],
};

export default config;
