/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_MARKET_OVERVIEW_POWERBI_URL?: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
