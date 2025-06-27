-- noinspection SqlCurrentSchemaInspectionForFile

-- Очистка всех таблиц с каскадным удалением зависимых данных
TRUNCATE TABLE
    agent_activities,
    agent_builds,
    agents,
    behavior_templates,
    roles
RESTART IDENTITY CASCADE;

-- === Таблица roles ===
INSERT INTO public.roles (name, description, category, is_active)
VALUES
  ('Agent', 'Standard agent role', 'agent', TRUE),
  ('Admin', 'Administrator role', 'admin', TRUE);

-- === Таблица behavior_templates ===
INSERT INTO public.behavior_templates (
    name, role_id, template_data, os_type, version, is_active
)
VALUES 
  (
    'Default Template',
    1,
    '{"tasks": ["open_browser", "simulate_activity"], "interval": 10}',
    'Windows',
    'v1.0',
    TRUE
  ),
  (
    'Simple Windows Tasks',
    1,
    '{"tasks": ["start_explorer", "start_calc", "simulate_activity"], "interval": 5}',
    'Windows',
    'v1.0',
    TRUE
  );

-- === Таблица agents ===
INSERT INTO public.agents (
    agent_id, name, role_id, template_id, status, os_type, config,
    injection_target, stealth_level, last_seen, last_activity
)
VALUES 
  (
    'agent_001',
    'Agent Smith',
    1,
    1,
    'active',
    'Windows',
    '{"interval": 1, "randomize": true}',
    'explorer.exe',
    'medium',
    NOW(),
    'launched browser'
  ),
  (
    'agent_002',
    'Agent Neo',
    1,
    2,
    'active',
    'Windows',
    '{"interval": 5, "randomize": false}',
    'calc.exe',
    'low',
    NOW(),
    'started calc'
  );

-- === Таблица agent_activities ===
INSERT INTO public.agent_activities (
    agent_id, activity_type, activity_data
)
VALUES 
  (
    1,
    'open_browser',
    '{"browser": "chrome", "url": "https://example.com"}'
  ),
  (
    2,
    'start_calc',
    '{"exe": "calc.exe"}'
  );

-- === Таблица agent_builds ===
INSERT INTO public.agent_builds (
    agent_id, build_config, binary_path, binary_size, build_status,
    build_log, build_time, completed_at
)
VALUES 
  (
    1,
    '{"target": "x64", "obfuscation": "basic"}',
    '/binaries/agent_001.exe',
    123456,
    'completed',
    'Build succeeded with no errors.',
    15,
    NOW()
  ),
  (
    2,
    '{"target": "x64", "obfuscation": "none"}',
    '/binaries/agent_002.exe',
    654321,
    'completed',
    'Build finished.',
    8,
    NOW()
  );
