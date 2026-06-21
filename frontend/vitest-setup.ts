import '@testing-library/jest-dom/vitest';

// Mock window.matchMedia
// This mock is robust enough for most UI libraries that use matchMedia for color scheme, etc.
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: vi.fn().mockImplementation((query) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: vi.fn(), // Deprecated but often used by older packages
    removeListener: vi.fn(), // Deprecated but often used by older packages
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
    dispatchEvent: vi.fn(),
  })),
});
