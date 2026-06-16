#!/usr/bin/env node
'use strict';

const { execSync } = require('child_process');
const os = require('os');
const path = require('path');

if (process.platform === 'win32') {
  console.error('boffyn does not support Windows.');
  process.exit(1);
}

// Ensure ~/.local/bin is in PATH so uv is found after installation
process.env.PATH = path.join(os.homedir(), '.local', 'bin') + path.delimiter + process.env.PATH;

function ensureUv() {
  try {
    execSync('uv --version', { stdio: 'ignore' });
  } catch {
    console.log('Installing uv...');
    execSync('curl -LsSf https://astral.sh/uv/install.sh | sh', { stdio: 'inherit', shell: true });
  }
}

ensureUv();

const { version } = require('../package.json');
execSync(`uv tool install boffyn==${version}`, { stdio: 'inherit', env: process.env });
