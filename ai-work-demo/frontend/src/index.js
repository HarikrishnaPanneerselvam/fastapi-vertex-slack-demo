import * as Sentry from "@sentry/react";
import { BrowserTracing } from "@sentry/tracing";


Sentry.init({
  dsn: "https://d328c16a92ae6661b8435920c825a9fe@o4510098511626240.ingest.us.sentry.io/4510103469359104",
  integrations: [new BrowserTracing()],
  tracesSampleRate: 1.0,
});
