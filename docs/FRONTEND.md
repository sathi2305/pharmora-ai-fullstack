# Frontend
Hierarchy: App (Next.js App Router ThemeProvider LanguageProvider) -> (auth)/login LoginForm+GoogleButton; (auth)/signup multi-step; (dashboard)/dashboard HealthScoreCard MyMedicinesWidget InteractionAlertsWidget VitalsTrendChart MediFloatingWidget; /medicines SearchBar PillScanner ResultsGrid MedicineDetailDrawer KG viz; /chat ChatHistory MessageBubble SuggestionChips VoiceInput; /health MetricTabs TrendChart LabUpload
State: Zustand useAuthStore useMedicineStore useChatStore useHealthStore useLanguageStore + React Query
Perf: dynamic Cytoscape, next/image, ISR, PWA