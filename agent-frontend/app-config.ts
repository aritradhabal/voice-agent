export interface AppConfig {
  pageTitle: string;
  pageDescription: string;
  companyName: string;

  supportsChatInput: boolean;
  supportsVideoInput: boolean;
  supportsScreenShare: boolean;
  isPreConnectBufferEnabled: boolean;

  logo: string;
  startButtonText: string;
  accent?: string;
  logoDark?: string;
  accentDark?: string;

  // for LiveKit Cloud Sandbox
  sandboxId?: string;
  agentName?: string;
}

export const APP_CONFIG_DEFAULTS: AppConfig = {
  companyName: 'Aritra Dhabal',
  pageTitle: 'aritra | Voice Agent',
  pageDescription: 'Talk with Aritra & see if he is right fit for you!',

  supportsChatInput: false,
  supportsVideoInput: false,
  supportsScreenShare: false,
  isPreConnectBufferEnabled: true,

  logo: '/me.png',
  accent: '#404040',
  logoDark: '/me.png',
  accentDark: '#fafaf9',
  startButtonText: 'Start Talking',

  // for LiveKit Cloud Sandbox
  sandboxId: undefined,
  agentName: undefined,
};
