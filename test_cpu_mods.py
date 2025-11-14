import torch
import os

# Test loading your checkpoint on CPU
checkpoint_path = 'checkpoints/wav2lip.pth'

print("Testing checkpoint loading...")
print(f"File exists: {os.path.exists(checkpoint_path)}")
print(f"File size: {os.path.getsize(checkpoint_path) / 1024 / 1024:.1f} MB")

try:
    # Try loading WITH map_location (should work)
    print("\n1. Loading with map_location='cpu'...")
    checkpoint = torch.load(checkpoint_path, map_location='cpu')
    print(f"✓ Success! Checkpoint keys: {list(checkpoint.keys())}")
    
    # Check what's inside
    if 'state_dict' in checkpoint:
        print(f"  - Has 'state_dict' key")
        print(f"  - Number of parameters: {len(checkpoint['state_dict'])}")
    else:
        print(f"  - Direct state dict (no wrapper)")
        print(f"  - Number of parameters: {len(checkpoint)}")
        
except Exception as e:
    print(f"✗ Failed: {e}")

# Also check PyTorch CUDA availability
print(f"\nCUDA available: {torch.cuda.is_available()}")
print(f"PyTorch version: {torch.__version__}")