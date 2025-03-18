# Release Process

## Steps to create a release:
1. **Prepare the code**:
   - Ensure all tests pass and that the code is in a stable state.
2. **Tag the version**:
   - Use the command `git tag -a vX.X.X -m "Release message"` to create a tag.
3. **Push the tag**:
   - Use `git push origin vX.X.X` to push the tag to the remote repository.
4. **Update documentation**:
   - Add release notes and update the README with the new version.
5. **Deploy to production**:
   - Follow deployment scripts or CI/CD pipeline for deploying to the production environment.

## Version Tagging Example:
- Tag: `v1.0.0`  
- Message: "First stable release with core IoT and dashboard features"
