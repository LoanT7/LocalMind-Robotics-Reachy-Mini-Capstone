# LocalMind Robotics - Project Progress

## September 2026

### Reachy Mini Simulator Setup

We successfully installed the Reachy Mini SDK and connected Python code to the Reachy Mini simulator.

We tested basic movement by controlling the robot's antennas.

### Local AI Setup

We tested an initial Hugging Face model but found that the response quality and latency were not good enough.

We then switched to Qwen2.5-0.5B-Instruct using llama.cpp and a quantized GGUF model.

Qwen was able to:

- Run locally
- Maintain basic conversation history
- Generate more useful responses
- Reach approximately 4-7.3 seconds total response latency

### AI + Reachy Integration

We successfully connected the local Qwen model to the Reachy Mini simulator.

Current working pipeline:

User types a message
→ Local Qwen AI
→ AI response
→ Text-to-speech
→ Reachy Mini movement

### Physical Robot

We also successfully established remote access to the physical Reachy Mini.

The next step is moving our working simulator pipeline into our own Reachy Mini application.