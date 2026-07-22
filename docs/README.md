# ArabPy Documentation

This directory contains the Docusaurus documentation for ArabPy.

## Development

### Install Dependencies

```bash
npm install
```

### Start Development Server

```bash
npm start
```

Visit `http://localhost:3000` to view the documentation.

### Build Documentation

```bash
npm run build
```

The built documentation will be in the `build/` directory.

### Serve Built Documentation

```bash
npm run serve
```

## Structure

- `docs/` - Documentation content in Markdown
- `src/` - Static assets and custom styling
- `docusaurus.config.ts` - Docusaurus configuration
- `sidebars.ts` - Documentation sidebar structure

## Adding Documentation

1. Create a new Markdown file in `docs/`
2. Add it to `sidebars.ts`
3. Follow the existing documentation style

## Deployment

Documentation is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the `main` branch.

## More Information

See [Docusaurus Documentation](https://docusaurus.io/docs) for more details.
