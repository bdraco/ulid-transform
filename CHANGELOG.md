# Changelog

<!--next-version-placeholder-->

## v0.9.0 (2023-10-18)

### Feature

* Build wheel with latest cpython release ([#25](https://github.com/bdraco/ulid-transform/issues/25)) ([`8bc67fe`](https://github.com/bdraco/ulid-transform/commit/8bc67fe8f2c56a9aacdede63331afe6c54a1528d))

### Fix

* Reduce size of wheels by excluding generated .cpp files ([#24](https://github.com/bdraco/ulid-transform/issues/24)) ([`29e0ff4`](https://github.com/bdraco/ulid-transform/commit/29e0ff474f729adea32c10a3d0adfc7801b5e892))

## v0.8.1 (2023-08-27)

### Fix

* Rebuild wheels with cython 3.0.2 ([#22](https://github.com/bdraco/ulid-transform/issues/22)) ([`8d78432`](https://github.com/bdraco/ulid-transform/commit/8d78432cf81b1a2e5230dd434b50c21365686548))

## v0.8.0 (2023-07-24)

### Feature

* Initial cpython 3.12 support ([#21](https://github.com/bdraco/ulid-transform/issues/21)) ([`7f7e8b9`](https://github.com/bdraco/ulid-transform/commit/7f7e8b90d3a7a529a58d00e66be8494a18476842))

## v0.7.2 (2023-05-01)
### Fix
* Ensure windows wheel work with older versions ([#20](https://github.com/bdraco/ulid-transform/issues/20)) ([`8a440e3`](https://github.com/bdraco/ulid-transform/commit/8a440e3f818b3af8a694544755d55f1c221ada3a))

## v0.7.1 (2023-05-01)
### Fix
* Missing decode for _bytes_to_ulid ([#19](https://github.com/bdraco/ulid-transform/issues/19)) ([`ddf6433`](https://github.com/bdraco/ulid-transform/commit/ddf6433554ca3d4fef6500b84e43adf475a794bb))

## v0.7.0 (2023-04-23)
### Feature
* Add a bytes_to_ulid cpp version ([#18](https://github.com/bdraco/ulid-transform/issues/18)) ([`fa1c62c`](https://github.com/bdraco/ulid-transform/commit/fa1c62c97be608390a5e42de5712382ee8ec86e9))

## v0.6.3 (2023-04-10)
### Fix
* Additional 32bit time fixes ([#17](https://github.com/bdraco/ulid-transform/issues/17)) ([`2f5f1be`](https://github.com/bdraco/ulid-transform/commit/2f5f1be3fe63bb63b57e158c32ab5e9d7ab16b9c))

## v0.6.2 (2023-04-09)
### Fix
* Apply 32bit cast for for random data ([#16](https://github.com/bdraco/ulid-transform/issues/16)) ([`1e1d62a`](https://github.com/bdraco/ulid-transform/commit/1e1d62aa961178d6416e4ac82cc0634b06260ad4))

## v0.6.1 (2023-04-09)
### Fix
* Apply 32bit time fix ([#15](https://github.com/bdraco/ulid-transform/issues/15)) ([`26347f0`](https://github.com/bdraco/ulid-transform/commit/26347f0067be94ba36607ea9b875b5d1354e6002))

## v0.6.0 (2023-04-06)
### Feature
* Reflect the invalid value when raising ValueError ([#13](https://github.com/bdraco/ulid-transform/issues/13)) ([`6a022fb`](https://github.com/bdraco/ulid-transform/commit/6a022fb4084e3a007c469e6e2993ccb3621c4271))

## v0.5.1 (2023-03-22)
### Fix
* Specify python version to build wheels ([#12](https://github.com/bdraco/ulid-transform/issues/12)) ([`9263de0`](https://github.com/bdraco/ulid-transform/commit/9263de0f70a4198cfcb2ba4a8f44440a7841e407))

## v0.5.0 (2023-03-22)
### Feature
* Wheels for macOS and Windows ([#11](https://github.com/bdraco/ulid-transform/issues/11)) ([`086852e`](https://github.com/bdraco/ulid-transform/commit/086852e57250994d0f3c9faedabf2df6aeb9e789))

## v0.4.2 (2023-03-13)
### Fix
* Ulid_now on 32bit ([#10](https://github.com/bdraco/ulid-transform/issues/10)) ([`c8f7dd7`](https://github.com/bdraco/ulid-transform/commit/c8f7dd790f987ca4310dd155a78fff263adf0cfc))

## v0.4.1 (2023-03-13)
### Fix
* Random as 0 on 32 bit arch ([#9](https://github.com/bdraco/ulid-transform/issues/9)) ([`c9fa4f3`](https://github.com/bdraco/ulid-transform/commit/c9fa4f32c12eabea67da14d0c32d9a5ac65f2842))

## v0.4.0 (2023-03-01)
### Feature
* Add bytes_to_ulid ([#8](https://github.com/bdraco/ulid-transform/issues/8)) ([`c9a57ef`](https://github.com/bdraco/ulid-transform/commit/c9a57ef2d68886d37e03dd9d884a51c35a5c1e12))

## v0.3.1 (2023-03-01)
### Fix
* Encode timestamps correctly in cpp implementation ([#7](https://github.com/bdraco/ulid-transform/issues/7)) ([`c7fedc3`](https://github.com/bdraco/ulid-transform/commit/c7fedc350bf9848dc38af362e33819fac4036a9e))

## v0.3.0 (2023-02-28)
### Feature
* Add examples ([#5](https://github.com/bdraco/ulid-transform/issues/5)) ([`be30a13`](https://github.com/bdraco/ulid-transform/commit/be30a133b3a03b1e6704954cf0c59f4fb64d4b7c))

## v0.2.1 (2023-02-28)
### Fix
* Drop fast-ulid for cython ([#4](https://github.com/bdraco/ulid-transform/issues/4)) ([`8d72d6b`](https://github.com/bdraco/ulid-transform/commit/8d72d6b58d306d722f096a5b3697d4365eae397d))

## v0.2.0 (2023-02-28)
### Feature
* Enable cython builds ([#3](https://github.com/bdraco/ulid-transform/issues/3)) ([`154bf0c`](https://github.com/bdraco/ulid-transform/commit/154bf0c8d02591508b87c2c154ba877da2aa8f97))

## v0.1.0 (2023-02-28)
### Feature
* Init repo ([#1](https://github.com/bdraco/ulid-transform/issues/1)) ([`0ef9511`](https://github.com/bdraco/ulid-transform/commit/0ef95113cd638617de16be44909b228d0df5f092))

### Fix
* Remove html file ([#2](https://github.com/bdraco/ulid-transform/issues/2)) ([`c1a5cf4`](https://github.com/bdraco/ulid-transform/commit/c1a5cf4a4a8c5a2c8ba1663b9132d612fe47570d))
